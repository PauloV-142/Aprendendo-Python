
def gen_inputs(inputs):
        """A generator that divides a string on every \\n.
        
        Stops yielding automatic inputs when finds a single line with a 'p', then it opens for user input.
        Said that, this is an infinite generator."""
        divide = lambda str, strToRemove: str.removeprefix(strToRemove).removesuffix(strToRemove).split(strToRemove)
        stop = False
        lenght = len(inputs)
        inputs = tuple(enumerate(divide(inputs, "\n")))
        for i, v in inputs:
            if not stop and v == "p" or i == lenght:
                stop = True
            if stop:
                yield input("user input: ")
                continue
                # raise StopIteration
            else:
                yield v
    


    
if __name__ == "__main__":
    str = """awoo
awii"""
    gen = gen_inputs(str)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    
        