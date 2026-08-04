from app.core.database import ScanDatabase
from tests.test_models import make_result


def test_database_save_load_delete(tmp_path) -> None:
    database = ScanDatabase(tmp_path / "history.sqlite3")
    result = make_result()
    database.save(result)
    summaries = database.list_summaries()
    assert summaries[0]["scan_id"] == result.scan_id
    loaded = database.load(result.scan_id)
    assert loaded is not None
    assert loaded.target == result.target
    database.delete(result.scan_id)
    assert database.load(result.scan_id) is None
