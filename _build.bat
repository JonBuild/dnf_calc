python _export_excel_to_txt.py

:: ʹ��pyinstaller���
pyinstaller.exe --hidden-import pkg_resources.py2_warn  --noconsole -F "�ٶ�ħ�İ�ʷʫװ��������_by��֮����.py"

:: �������ɵĽ����ɾ����ʱ�ļ�
COPY /Y "dist\�ٶ�ħ�İ�ʷʫװ��������_by��֮����.exe" "�ٶ�ħ�İ�ʷʫװ��������_by��֮����.exe"
RMDIR /S /Q "build" "dist" "__pycache__"
DEL /Q "�ٶ�ħ�İ�ʷʫװ��������_by��֮����.spec"
