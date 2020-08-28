import subprocess
import sys


# needs ffmpeg and ffprobe on path of the machine

class SoundCloudDownloader(object):
    def download(self, url, path, debug=False):
        # --exec \'move {} ' + path + '\' '
        c = subprocess.Popen(
            r'youtube-dl.exe --restrict-filenames  -x  --audio-quality 320K --audio-format mp3 --exec "move {} ' + path + r'\{}" --output %(uploader)s-%(title)s.%(ext)s ' + url,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = c.communicate()
        if debug:
            print(err)
        return out


if __name__ == '__main__':
    downloader = SoundCloudDownloader()
    downloader.download(sys.argv[1], '.', debug=True)
