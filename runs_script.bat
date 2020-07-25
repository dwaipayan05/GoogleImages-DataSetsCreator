@ECHO OFF

python FileTransfer.py
python MergeFiles.py
python Downloader_With_PreProcess.py --urls MasterURL.txt --output F:\Projects\Personal\DataSetsMerger\Images

PAUSE