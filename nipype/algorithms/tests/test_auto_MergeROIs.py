# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..misc import MergeROIs


def test_MergeROIs_inputs():
    input_map = dict(in_files=dict(),
    in_index=dict(),
    in_reference=dict(),
    )
    inputs = MergeROIs.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_MergeROIs_outputs():
    output_map = dict(merged_file=dict(),
    )
    outputs = MergeROIs.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
