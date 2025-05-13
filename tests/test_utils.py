import json
import pytest

from orcbundle.utils.general import get_project_root


@pytest.fixture
def get_context_mock() -> dict:
        context_ref = get_project_root() / "resources/bundles/bund1.json"
        with open(context_ref, "r", encoding='utf-8') as f:
            context_expected = json.load(f)
        return context_expected