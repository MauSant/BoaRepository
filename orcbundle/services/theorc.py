from datetime import timedelta
import json
import logging
from typing import Any
import uuid
import asyncio

from temporalio.client import Client

from orcbundle.utils.constants import TASK_QUEUE


async def start_theorc_workflow(orc_request: dict[str,Any]) -> None:

    # Connect client
    client = await Client.connect("localhost:7233")

    # Run workflow
    result = await  client.execute_workflow(
        "THE_ORC",
        arg=orc_request,
        id=f"orc-workflow-id-{uuid.uuid4()}",
        task_queue=TASK_QUEUE
    )
    print()


