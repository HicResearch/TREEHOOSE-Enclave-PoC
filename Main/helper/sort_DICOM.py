# original code from Alex Weston
# Digital Innovation Lab, Mayo Clinic

import os
import pydicom  # pydicom is using the gdcm package for decompression


def clean_text(string):
    # clean and standardize text descriptions, which makes searching files easier
    forbidden_symbols = ["*", ".", ",", "\"", "\\", "/", "|", "[", "]", ":", ";", " "]
    for symbol in forbidden_symbols:
        string = string.replace(symbol, "_")  # replace everything with an underscore
    return string.lower()


# user specified parameters
src  = '/home/ubuntu/studies/u-2i9S6_cORA1vaGucELFdF/AWS_WP3/DICOM/ffa0037427'
dst = '/home/ubuntu/studies/u-2i9S6_cORA1vaGucELFdF/AWS_WP3/DICOM/ffa0037427_sorted' #"/home/m081739/projects/RSNA_temp/sorted"

# sort studies  into different series
def sort_DICOM(src, dst):
    print('reading file list...')
    unsortedList = []
    for root, dirs, files in os.walk(src):
        for file in files:
            if ".dcm" in file:  # exclude non-dicoms, good for messy folders
                unsortedList.append(os.path.join(root, file))

    print('%s files found.' % len(unsortedList))

    for dicom_loc in unsortedList:
        # read the file
        ds = pydicom.read_file(dicom_loc, force=True)

        # get patient, study, and series information
        patientID = clean_text(ds.get("PatientID", "NA"))
        studyDate = clean_text(ds.get("StudyDate", "NA"))
        studyDescription = clean_text(ds.get("StudyDescription", "NA"))
        seriesDescription = clean_text(ds.get("SeriesDescription", "NA"))
        ##added series ID
        seriesInstanceUID = ds.get("SeriesInstanceUID", "NA")

        # generate new, standardized file name
        modality = ds.get("Modality", "NA")
        studyInstanceUID = ds.get("StudyInstanceUID", "NA")
        seriesInstanceUID = ds.get("SeriesInstanceUID", "NA")
        instanceNumber = str(ds.get("InstanceNumber", "0"))
        fileName = modality + "." + seriesInstanceUID + "." + instanceNumber + ".dcm"

        # uncompress files (using the gdcm package)
        try:
            ds.decompress()
        except:
            print('an instance in file %s - %s - %s - %s" could not be decompressed. exiting.' % (
            #patientID, studyDate, studyDescription, seriesDescription)) replace seriesDescription by series ID
            patientID, studyDate, studyDescription, seriesInstanceUID))

        # save files to a 4-tier nested folder structure
        if not os.path.exists(os.path.join(dst, patientID)):
            os.makedirs(os.path.join(dst, patientID))

        if not os.path.exists(os.path.join(dst, patientID, studyDate)):
            os.makedirs(os.path.join(dst, patientID, studyDate))

        if not os.path.exists(os.path.join(dst, patientID, studyDate, studyDescription)):
            os.makedirs(os.path.join(dst, patientID, studyDate, studyDescription))

        if not os.path.exists(os.path.join(dst, patientID, studyDate, studyDescription, seriesInstanceUID)):
            os.makedirs(os.path.join(dst, patientID, studyDate, studyDescription, seriesInstanceUID))
            print('Saving out file: %s - %s - %s - %s.' % (patientID, studyDate, studyDescription, seriesInstanceUID))

        ds.save_as(os.path.join(dst, patientID, studyDate, studyDescription, seriesInstanceUID, fileName))

    print('done.')