"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import CloseApproach, NearEarthObject


def load_neos(neo_csv_path='data/neos.csv'):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    with open(neo_csv_path) as infile:
        reader = csv.DictReader(infile)
        return [
            NearEarthObject(
                designation=neo['pdes'],
                name=neo['name'],
                diameter=neo['diameter'],
                hazardous=neo['pha']
            ) for neo in reader
        ]


def load_approaches(cad_json_path='data/cad.json'):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path) as infile:
        content = json.load(infile)
        approaches = content['data']
        return [
            CloseApproach(
                designation=ca[0],
                time=ca[3],
                distance=ca[4],
                velocity=ca[7]
            ) for ca in approaches
        ]
