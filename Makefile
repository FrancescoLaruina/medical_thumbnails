DEST:=/usr/local/bin
THUMB_FOLDER:=${HOME}/.local/share/thumbnailers
MIME:=${HOME}/.local/share/mime

install: clean_cache
	pip install -r requirements.txt
	cp ${CURDIR}/medical_thumbnails/thumbnailer.py ${DEST}/medical_thumbnailer
	mkdir -p ${MIME}/packages/
	cp ${CURDIR}/medical_thumbnails/nii.xml ${MIME}/packages/
	update-mime-database ${MIME}
	mkdir -p ${THUMB_FOLDER}
	cp ${CURDIR}/medical_thumbnails/medical.thumbnailer ${THUMB_FOLDER}/
	echo "Installation completed"

uninstall:
	rm ${DEST}/medical_thumbnailer
	rm ${THUMB_FOLDER}/medical.thumbnailer
	rm ${MIME}/packages/nii.xml

update: uninstall install

clean_cache:
	rm -rf ${HOME}/.cache/thumbnails/fail
test:
	. $(CURDIR)/set_pythonpath.sh && pytest-3
