import pytest
from unittest.mock import Mock, MagicMock
from datetime import datetime
from fastapi import HTTPException, UploadFile
from io import BytesIO

from src.routes.posts import create_post, get_posts
from src import models


class TestCreatePost:

    @pytest.mark.asyncio
    async def test_create_post_without_image(self, mocker):
        # Setup mock database
        mock_db = Mock()
        mock_post = Mock(spec=models.Post)
        mock_post.id = 1
        mock_post.title = "Lost Wallet"
        mock_post.category = "lost"
        
        mocker.patch('src.routes.posts.models.Post', return_value=mock_post)
        
        result = await create_post(
            title="Lost Wallet",
            description="Black leather wallet",
            category="lost",
            location="Library",
            date="2025-11-20",
            contactName="John Doe",
            contact="john@example.com",
            image=None,
            db=mock_db
        )
        
        mock_db.add.assert_called_once()
        mock_db.commit.assert_called_once()
        assert result == mock_post

    @pytest.mark.asyncio
    async def test_create_post_with_image(self, mocker):
        mock_db = Mock()
        
        # Mock image file
        mock_image_file = Mock(spec=UploadFile)
        mock_image_file.content_type = "image/png"
        mock_image_file.filename = "test.png"
        mock_image_file.file = BytesIO(b"fake_data")
        
        # Mock PIL Image
        mock_pil_image = MagicMock()
        mocker.patch('src.routes.posts.Image.open', return_value=mock_pil_image)
        mock_pil_image.__enter__ = Mock(return_value=mock_pil_image)
        mock_pil_image.__exit__ = Mock(return_value=False)
        mock_pil_image.convert = Mock(return_value=mock_pil_image)
        mock_pil_image.thumbnail = Mock()
        mock_pil_image.save = Mock()
        
        # Mock file operations
        mocker.patch('src.routes.posts.uuid4', return_value='abc123')
        mocker.patch('src.routes.posts.os.path.join', side_effect=lambda *args: '/'.join(args))
        mocker.patch('src.routes.posts.os.makedirs')
        mocker.patch('src.routes.posts.os.path.splitext', return_value=('test', '.png'))
         
        # Mock Post
        mock_post = Mock(spec=models.Post)
        mock_post.id = 1
        mock_post.image_path = "uploads/abc123.png"
        mocker.patch('src.routes.posts.models.Post', return_value=mock_post)
        
        result = await create_post(
            title="Lost Keys",
            description="Car keys",
            category="lost",
            location="Parking",
            date="2025-11-20",
            contactName="Jane",
            contact="555-1234",
            image=mock_image_file,
            db=mock_db
        )
        
        # Verify mocks were called
        mock_pil_image.convert.assert_called_once_with("RGB")
        mock_pil_image.thumbnail.assert_called_once()
        mock_db.add.assert_called_once()
        mock_db.commit.assert_called_once()
        assert result.image_path == "uploads/abc123.png"

    @pytest.mark.asyncio
    async def test_invalid_category_error(self, mocker):
        mock_db = Mock()
        
        with pytest.raises(HTTPException) as exc:
            await create_post(
                title="Test",
                description="Test",
                category="wrong",
                location="Test",
                date="2025-11-20",
                contactName="Test",
                contact="test@test.com",
                image=None,
                db=mock_db
            )
        
        assert exc.value.status_code == 400


class TestGetPosts:

    def test_get_posts(self, mocker):
        mock_db = Mock()
        
        mock_post = Mock(spec=models.Post)
        mock_post.id = 1
        
        mock_query = Mock()
        mock_order = Mock()
        
        mock_db.query.return_value = mock_query
        mock_query.order_by.return_value = mock_order
        mock_order.all.return_value = [mock_post]
        
        result = get_posts(db=mock_db)
        
        assert len(result) == 1
        mock_db.query.assert_called_once()

