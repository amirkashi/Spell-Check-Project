class read_file():
    def __init__(self, input_file):
        self.input_file = input_file
        self.word_list = []
        self.tag_list = []
    
    def make_wort_and_tag_lists(self):
        read_lines = open(self.input_file, 'r')
        for line in read_lines:
            line = line.strip()
            if "\t" in line:
                line = line.split()
                self.word_list.append(line[0])
                self.tag_list.append(line[1])
        return self.word_list, self.tag_list
