from subprocess import Popen, PIPE
import threading
import os
import signal


# def exec_cmd(cmd, interact=False):...

class Command():
  """Python 2.7.5 带有超时功能的 subprocess"""
    status = -1
    output = error = ""

    def __init__(self):
        self.process = None

    def run(self, cmd, timeout=60):
        def target():
            self.process = Popen(cmd, shell=True, stdin=PIPE,
                                stderr=PIPE, stdout=PIPE, preexec_fn=os.setsid)
            self.output, self.error = self.process.communicate()
            self.output = self.output.strip()
            self.status = self.process.returncode

        thread = threading.Thread(target=target)
        thread.start()
        thread.join(timeout)
        if thread.is_alive():
            os.killpg(self.process.pid, signal.SIGTERM)
            thread.join()
        return self.status, self.output, self.error
