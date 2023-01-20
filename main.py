class Stack():
    def __init__(self):
        self.current_stack = []

    def isEmpty(self):
        return self.current_stack == []

    def push(self, add_element):
        self.current_stack.insert(0, add_element)

    def pop(self):
        if self.isEmpty() is False:
            return self.current_stack.pop(0)
        else:
            return False

    def peek(self):
        if self.isEmpty() is False:
            return self.current_stack[0]
        else:
            return False

    def size(self):
        return len(self.current_stack)

    def show(self):
        return self.current_stack


def stack_check(str):
    unbalanced_sequences = ['(]', '[)', '[}', '{]', '(}', '{)']
    for seq in unbalanced_sequences:
        if seq in str:
            return 'несбалансирована'

    braces_list = list(str)

    braces = Stack()  # фигурные скобки
    round_brackets = Stack()  # круглые скобки
    square_brackets = Stack()  # квадратные скобки

    for elem in braces_list:
        if elem == '(':
            round_brackets.push(elem)
        elif elem == ')':
            if round_brackets.peek() is False:
                return 'несбалансирована'
            else:
                round_brackets.pop()
        elif elem == '[':
            square_brackets.push(elem)
        elif elem == ']':
            if square_brackets.peek() is False:
                return 'несбалансирована'
            else:
                square_brackets.pop()
        elif elem == '{':
            braces.push(elem)
        elif elem == '}':
            if braces.peek() is False:
                return 'несбалансирована'
            else:
                braces.pop()

    if braces.size() == 0 and round_brackets.size() == 0 and square_brackets.size() == 0:
        return 'сбалансирована'
    else:
        return False


if __name__ == '__main__':

    # Cбалансированные  последовательности:
    a = '(((([{}]))))'
    b = '[([])((([[[]]])))]'
    c = '{()}'
    d = '{{[()]}}'

    print(f'Последовательность a {stack_check(a)}')
    print(f'Последовательность b {stack_check(b)}')
    print(f'Последовательность c {stack_check(c)}')
    print(f'Последовательность d {stack_check(d)}')

    print('-----------------------------------------')

    # Несбалансированные последовательности:
    e = '}{}'
    f = '{{[(])]}}'
    g = '[[{())}]'

    print(f'Последовательность e {stack_check(e)}')
    print(f'Последовательность f {stack_check(f)}')
    print(f'Последовательность g {stack_check(g)}')
