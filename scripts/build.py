import subprocess

def main():
    subprocess.run([
        "pyinstaller",
        "--name", "network-capture",
        "--onefile", "network_activity_stream/main.py"
    ], check=True)

if __name__ == "__main__":
    main()
