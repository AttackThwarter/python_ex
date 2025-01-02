# write context manager to read one file and write to another file


class MultiFileManager:

    def __init__(self, input_file: str, output_file: str, w_mod) -> None:
        self.input_file_path = input_file
        self.output_file_path = output_file
        self.w_mod = w_mod


    def __enter__(self):

        self.input_file = open(self.input_file_path, 'r')
        self.output_file = open(self.output_file_path, self.w_mod)

        print(f"open {self.input_file_path} and {self.output_file_path}")

        return self

    def __exit__(self, exc_type, exc_value, trace):

        if self.input_file:
            self.input_file.close()
            print(f"File {self.input_file_path} closed")

        if self.output_file:
            self.output_file.close()
            print(f"File {self.output_file_path} closed")



        if exc_type:
            print(f"exception raised {exc_value}")
        return False  




with MultiFileManager("r_test.txt", "w_test.txt", w_mod="w+") as manager:
    
    for line in manager.input_file:
        if len(line) > 50:
            print("find +50 chars line")
        manager.output_file.write(line)
