:: ����ǰ���������͵�github
call _git_push_remote.bat

:: ���ù����ű������
call _build.bat

:: ����Ŀ��Ŀ¼
set target_dir=.\..\..\..\downloads\(����ħ�ļ�����\�ٶ�ħ�İ�ʷʫװ��������_v��дʵ�ʵ�С�汾��_by��֮����

:: ɾ��Ŀ��Ŀ¼���ؽ�
RMDIR /S /Q "%target_dir%"
MKDIR %target_dir%

:: �������ļ����Ƶ�Ŀ��Ŀ¼
XCOPY ".\*.*" "%target_dir%" /S /E /Y

:: ��ת��Ŀ��Ŀ¼
cd "%target_dir%"

:: �Ƴ�һЩ���跢�����ļ����Լ���ʼ����ش浵
xcopy preset_clear.XLSX preset.XLSX /Y/B
RMDIR /S /Q ".git" ".idea"
DEL /Q "DATA - ����.xlsx" "preset_clear.XLSX" "test.py" �����н��.xlsx��
ren "ħ�ĺ�.py__" "ħ�ĺ�.py"
ren "calc.py__" "calc.py"
