CURRENT_DIR:=$(dir $(abspath $(MAKEFILE_LIST)))
DEST:=/usr/local/bin
THUMB_FOLDER:=${HOME}/.local/share/thumbnailers

install:
	cp ${CURRENT_DIR}/medical_thumbnails/thumbnailer.py ${DEST}/medical_thumbnailer
	mkdir -p ${THUMB_FOLDER}
	cp $(CURRENT_DIR)/medical_thumbnails/medical.thumbnailer $(THUMB_FOLDER)/
uninstall:
	rm ${DEST}/medical_thumbnailer ${THUMB_FOLDER}/medical.thumbnailer

clean_cache:
	rm -rf ${HOME}/.cache/thumbnails/fail
