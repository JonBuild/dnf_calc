@ECHO OFF

:: �޸�consoleĬ��encodingΪutf8��������������
CHCP 65001
CLS

echo.
echo [��ʾ]: ����excelΪtxt������汾�Ա�
echo.

python _export_excel_to_txt.py


echo.
echo [��ʾ]: ��ʼ���
echo.


:: ʹ��pyinstaller���
pyinstaller.exe --hidden-import pkg_resources.py2_warn  --noconsole -F "�ٶ�ħ�İ�ʷʫװ��������_by��֮����.py"

:: �������ɵĽ����ɾ����ʱ�ļ�
COPY /Y "dist\�ٶ�ħ�İ�ʷʫװ��������_by��֮����.exe" "�ٶ�ħ�İ�ʷʫװ��������_by��֮����.exe"
RMDIR /S /Q "build" "dist" "__pycache__"
DEL /Q "�ٶ�ħ�İ�ʷʫװ��������_by��֮����.spec"


echo.
echo [��ʾ]: �������
echo.
