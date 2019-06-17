import subprocess

videos = [
    'https://www.youtube.com/watch?v=vAIj0tikZH4',
    'https://www.youtube.com/watch?v=Wz_f9B4pPtg'
]


def get_video(youtube_url, output_path):
    # tmpd = tempfile.mkdtemp()
    command = (f'youtube-dl -f best --output "{output_path}/%(id)s.%(ext)s" {youtube_url}')

    print(command)
    _ = subprocess.run([command], check=False, shell=True, stdout=subprocess.PIPE)
    # asp = load_asp_files(tmpd)
    # shutil.rmtree(tmpd)
    # return asp.get(video_id, {})


if __name__ == "__main__":
    for v in videos:
        get_video(v, 'data')
