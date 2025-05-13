import pytest
import sys

from orcbundle.models.bundle import (
    ActionTypes,
    HttpAction,
    HTTPMethods,
    Bundle,
)

from tests.test_utils import get_context_mock



# def test_asdict_compound_classes(orc_request_mock,
#  get_context_mock)="",
#         result = orc_request_mock.dict()
#         get_context_mock.pop("run_id")
#         get_context_mock.pop("action_outputs")

#         assert result == get_context_mock


def test_http_action_model():
    http_model = HttpAction(
        action_type=ActionTypes.HTTP,
        name="",
        url="",
        http_method=HTTPMethods.GET,
    )

    print()

def test_bundle(get_context_mock):
    print()
    bundle = Bundle(**get_context_mock)
    print()


if __name__ == "__main__":
    pytest.main(sys.argv)