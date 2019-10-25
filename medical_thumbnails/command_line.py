"""CLI interface for the thumbnailer"""
from medical_thumbnails import utils

PARSER = utils.build_parser()
ARGS = PARSER.parse_args()
IMG = utils.load_dicom(ARGS.inp)
utils.save_thumbnail(IMG, ARGS.out, ARGS.size)
