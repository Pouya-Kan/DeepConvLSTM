import sys,json

f = open('DeepConvLSTM.ipynb', 'r')  # input.ipynb
j = json.load(f)
of = open('deep_conv_LSTM.py', 'w')  # output.py

if j["nbformat"] >=4:
    for i,cell in enumerate(j["cells"]):
            of.write("#cell "+str(i)+"\n")
            for line in cell["source"]:
                    of.write(line)
            of.write('\n\n')
else:
    print('salam')
    print(j["worksheets"][0])
    for i,cell in enumerate(j["worksheets"][0]["cells"]):
            of.write("#cell "+str(i)+"\n")
            try:
                for line in cell["input"]:
                        of.write(line)
                of.write('\n\n')
            except KeyError:
                pass

of.close()
