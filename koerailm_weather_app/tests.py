import pytest
from koerailm_weather_app.models import FolkSaying


@pytest.mark.django_db
def test_create_folk_saying():
    folk_saying = FolkSaying.objects.create(text="Test folk saying")
    assert folk_saying.id is not None
    assert folk_saying.text == "Test folk saying"


@pytest.mark.django_db
def test_read_folk_saying():
    folk_saying = FolkSaying.objects.create(text="Test folk saying")
    retrieved_folk_saying = FolkSaying.objects.get(id=folk_saying.id)
    assert retrieved_folk_saying.text == "Test folk saying"


@pytest.mark.django_db
def test_update_folk_saying():
    folk_saying = FolkSaying.objects.create(text="Old saying")
    folk_saying.text = "Updated saying"
    folk_saying.save()
    updated_folk_saying = FolkSaying.objects.get(id=folk_saying.id)
    assert updated_folk_saying.text == "Updated saying"


@pytest.mark.django_db
def test_delete_folk_saying():
    folk_saying = FolkSaying.objects.create(text="Saying to delete")
    folk_saying_id = folk_saying.id
    folk_saying.delete()
    with pytest.raises(FolkSaying.DoesNotExist):
        FolkSaying.objects.get(id=folk_saying_id)


@pytest.mark.django_db
def test_list_folk_sayings():
    FolkSaying.objects.create(text="First folk saying")
    FolkSaying.objects.create(text="Second folk saying")
    folk_sayings = FolkSaying.objects.all()
    assert len(folk_sayings) == 2
