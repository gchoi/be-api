#!/usr/bin/env python

# Module imports
import cv2
import base64
from logger import logging
from fastapi import FastAPI, Body
from typing import List

# Custom module imports
# from app.model import DateAvailable, Item
from app.model import Point, BoundingBoxPoints, MatchingCad, Block, PeYard

app = FastAPI()


# --- [GET] date available for the month
@app.get("/date-available/", tags=["date-available"])
async def get_date_available(yyyymm: str) -> List[int]:

    """
    Gets the list of the dates available for the requested month.

    Args
    -------
    - yyyymm (str):   requested month, ex) 202308

    Returns
    -------
    -   List of the dates available in the month: List(int)
    """

    logging.info("Requested for dates available: {yyyymm}")

    # TODO: find the available dates of the requested month
    example_return = [1, 2, 3, 4, 5]

    return example_return


# --- [PUT] ground truth update
@app.put("/gt-update/", tags=["gt-update"])
async def update_ground_truth(
    block_id: str,
    cad_id: str
) -> List[Block]:

    """
    Updates the ground truth for the block-CAD matching candidates.

    Args
    -------
    - block_id (str): ID of the requested block
    - cad_id (str):   ID of the CAD to set as ground truth

    Returns
    -------
    - List of the blocks updated: List[Block]
    """

    logging.info("Requested for ground-truth update.")
    logging.info(f"block_id: {block_id}, cad_id: {cad_id}")

    # TODO: update the block ground truth
    img_path = './images/2361_20G_208_0.png'
    img = cv2.imread(img_path)
    encoded = base64.b64encode(img)

    example_return = [
        Block(
            block_id='2361_20G_637',
            status='normal',
            image=encoded,
            bounding_boxes=[
                BoundingBoxPoints(
                    points=Point(
                        x=100,
                        y=200
                    )
                ),
                BoundingBoxPoints(
                    points=Point(
                        x=100,
                        y=200
                    )
                ),
                BoundingBoxPoints(
                    points=Point(
                        x=100,
                        y=200
                    )
                ),
                BoundingBoxPoints(
                    points=Point(
                        x=100,
                        y=200
                    )
                ),
                BoundingBoxPoints(
                    points=Point(
                        x=100,
                        y=200
                    )
                )
            ],
            matching_cads=[
                MatchingCad(
                    cad_id='2361_50G_528_2',
                    image=encoded,
                    gt=False
                ),
                MatchingCad(
                    cad_id='2361_50G_528_2',
                    image=encoded,
                    gt=False
                ),
                MatchingCad(
                    cad_id='2361_50G_528_2',
                    image=encoded,
                    gt=False
                ),
                MatchingCad(
                    cad_id='2361_50G_528_2',
                    image=encoded,
                    gt=False
                ),
                MatchingCad(
                    cad_id='2361_50G_528_2',
                    image=encoded,
                    gt=False
                )
            ]
        )
    ]

    return example_return


# --- [GET] List of P.E. Yard data (am/pm) for requested date
@app.get("/yard-data/", tags=["yard-data"])
async def get_yard_data(
    yyyymmdd: str
) -> List[PeYard]:

    """
    Gets the P.E. Yard data (am/pm) for the requested date.

    Args
    -------
    - yyyymmdd (str): ID of the requested block
    - cad_id (str):   ID of the CAD to set as ground truth

    Returns
    -------
    - List of the blocks updated: List[Block]
    """

    logging.info("Requested for P.E. yard data.")
    logging.info(f"yyyymmdd: {yyyymmdd}")

    img_path = './images/2361_20G_208_0.png'
    img = cv2.imread(img_path)
    encoded = base64.b64encode(img)

    example_return = [
        PeYard(
            yard_id='20221031_pm',
            location='DOCK1',
            image=encoded,
            blocks=[
                Block(
                    block_id='2361_20G_637',
                    status='delayed+3',
                    image=encoded,
                    bounding_boxes=[
                        BoundingBoxPoints(
                            points=Point(
                                x=100,
                                y=200
                            )
                        ),
                        BoundingBoxPoints(
                            points=Point(
                                x=100,
                                y=200
                            )
                        )
                    ],
                    matching_cads=[
                        MatchingCad(
                            cad_id='1',
                            image=encoded,
                            gt=False
                        ),
                        MatchingCad(
                            cad_id='2',
                            image=encoded,
                            gt=True
                        )
                    ]
                )
            ]
        ),
        PeYard(
            yard_id='20221031_pm',
            location='DOCK1',
            image=encoded,
            blocks=[
                Block(
                    block_id='2361_20G_637',
                    status='delayed+3',
                    image=encoded,
                    bounding_boxes=[
                        BoundingBoxPoints(
                            points=Point(
                                x=100,
                                y=200
                            )
                        ),
                        BoundingBoxPoints(
                            points=Point(
                                x=100,
                                y=200
                            )
                        )
                    ],
                    matching_cads=[
                        MatchingCad(
                            cad_id='1',
                            image=encoded,
                            gt=False
                        ),
                        MatchingCad(
                            cad_id='2',
                            image=encoded,
                            gt=True
                        )
                    ]
                )
            ]
        )
    ]

    return example_return
