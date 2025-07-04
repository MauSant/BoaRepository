from datetime import timedelta
import json
import logging
from typing import Any
import uuid
import asyncio

from temporalio.client import Client

from orcbundle.utils.constants import TASK_QUEUE


async def start_boa_simulator_workflow(orc_request: dict[str,Any]) -> None:

    # Connect client
    client = await Client.connect("localhost:7233")
    wfid = f"boa-simulator-id-{uuid.uuid4()}"

    # Run workflow
    result = await  client.start_workflow(
    # .execute_workflow(
        "THE_ORC",
        arg=orc_request,
        id=wfid,
        task_queue=TASK_QUEUE
    )
    url = f"http://localhost:8080/namespaces/default/workflows/{wfid}/{result.result_run_id}/history"

    return url


