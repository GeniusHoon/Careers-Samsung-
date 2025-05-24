import os
import subprocess

### PROMPT
python을 이용해서 현재 실행 경로에 있는 모든 ipynb 파일을 pdf로 변환하는 코드를 작성해줘
###

def convert_ipynb_to_pdf():
    """
    현재 실행 경로에 있는 모든 .ipynb 파일을 PDF로 변환합니다.
    """
    current_directory = os.getcwd()
    print(f"현재 디렉토리: {current_directory}")

    ipynb_files = [f for f in os.listdir(current_directory) if f.endswith('.ipynb')]

    if not ipynb_files:
        print("현재 디렉토리에 .ipynb 파일이 없습니다.")
        return

    print(f"변환할 .ipynb 파일: {ipynb_files}")

    for ipynb_file in ipynb_files:
        file_name_without_ext = os.path.splitext(ipynb_file)[0]
        output_pdf_path = os.path.join(current_directory, f"{file_name_without_ext}.pdf")

        try:
            # nbconvert 명령 실행
            # --to webpdf를 사용하면 더 나은 PDF 출력을 얻을 수 있습니다. (Chromium 필요)
            # 만약 webpdf가 작동하지 않거나 설치하기 어렵다면, --to pdf를 사용하세요.
            # 이 경우 LaTeX (xelatex, pdflatex 등) 설치가 필요할 수 있습니다.
            command = ["jupyter", "nbconvert", "--to", "webpdf", ipynb_file, "--output-dir", current_directory]
            # command = ["jupyter", "nbconvert", "--to", " "pdf", ipynb_file, "--output-dir", current_directory] # LaTeX 필요

            print(f"\n'{ipynb_file}' 파일을 PDF로 변환 중...")
            process = subprocess.run(command, check=True, capture_output=True, text=True)
            print(f"변환 성공: '{output_pdf_path}'")
            print("--- 변환 출력 ---")
            print(process.stdout)
            if process.stderr:
                print("--- 변환 에러 (경고일 수 있음) ---")
                print(process.stderr)

        except subprocess.CalledProcessError as e:
            print(f"오류 발생: '{ipynb_file}' 파일을 PDF로 변환하는 데 실패했습니다.")
            print(f"에러 메시지: {e}")
            print(f"표준 출력: {e.stdout}")
            print(f"표준 에러: {e.stderr}")
        except FileNotFoundError:
            print("오류: 'jupyter' 명령을 찾을 수 없습니다. 'nbconvert'가 설치되었는지 확인하고, PATH에 추가되었는지 확인하세요.")
        except Exception as e:
            print(f"예상치 못한 오류 발생: {e}")

if __name__ == "__main__":
    convert_ipynb_to_pdf()
