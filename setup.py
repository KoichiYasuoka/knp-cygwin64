import setuptools
import glob
import platform
if platform.system().startswith("CYGWIN") and platform.machine()=="x86_64":
  import subprocess
  subprocess.run(["sh","-x","./unxzall.sh"])
else:
  raise OSError("knp-cygwin64 only for 64-bit Cygwin")

class PostInstall(setuptools.command.install.install):
  def run(self):
    install.run(self)
    import subprocess
    subprocess.run(["touch","-r","/usr/local/knp/dict/crf.model","/usr/local/knp/rule/*"])

setuptools.setup(
  name="knp-cygwin64",
  version="0.4.0",
  packages=setuptools.find_packages(),
  data_files=[
    ("local/bin",glob.glob("bin/*")),
    ("local/libexec/knp",glob.glob("libexec/knp/*")),
    ("local/lib",glob.glob("lib/*")),
    ("local/etc",glob.glob("etc/*")),
    ("local/include",glob.glob("include/*")),
    ("local/share/knp/dict",glob.glob("share/knp/dict/*.model")),
    ("local/share/knp/dict/auto",glob.glob("share/knp/dict/auto/*.db")),
    ("local/share/knp/dict/distsim",glob.glob("share/knp/dict/distsim/*.db")),
    ("local/share/knp/dict/gcf",glob.glob("share/knp/dict/gcf/*.db")),
    ("local/share/knp/dict/synonym",glob.glob("share/knp/dict/synonym/*.db")),
    ("local/share/knp/dict/ebcf",glob.glob("share/knp/dict/ebcf/*.d*[bt]")),
    ("local/share/knp/rule",glob.glob("share/knp/rule/*")),
    ("local/share/knp/doc",glob.glob("share/knp/doc/*"))
  ],
  install_requires=["juman-cygwin64@git+https://github.com/KoichiYasuoka/juman-cygwin64"],
  cmdclass={"install":PostInstall}
)
