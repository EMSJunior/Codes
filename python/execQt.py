import os



onlyfiles = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]


for i in onlyfiles:
  if(i[len(i)-2::] == 'ui'):
      qtnome = i[0:len(i)-3]
      os.system('python -m PyQt5.uic.pyuic -x '+os.getcwd()+'\\'+qtnome+'.ui -o '+os.getcwd()+'\\'+qtnome+'.py')