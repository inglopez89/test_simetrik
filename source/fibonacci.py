
class TestFibonacci:
    """
    This class is get the fk value where a fibonacci value in its
    first and last 9 number its pan digital
    params:
    n_series: Is a number for get the number fibonacci.
    """
    def __init__(self, n_series):
        self.n_series = n_series

    def __ispandigital(self, n):
        """
        This is a private method evaluated is the validate if a number is pan digital
        ---
        param
        n: the list with the number for validate
        return
        len of list values whitout duplicate values
        """
        try:
            pan_digital = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            validate = [s for p in pan_digital for s in n if int(s) == p]
            return len(set(validate))
        except Exception as e:
            print('An error has occurred for fn ispandigital: ', e)

    def fk(self):
        """
        This method is for create fibonacci series
        ---
        Params
        fn1: is the first value of fibonacci
        fn2: is the second value of fibonacci
        Return
        n: number of fibonacci
        num: number for iter and find fibonacci values
        """
        try:
            # initial fibonacci
            fn1 = 1
            fn2 = 1
            # seeking fibonacci number
            num = self.n_series
            # iter while number is more than 2, because the initial fibonacci is 1,1
            while num > 2:
                # calculate fibonacci for two last numbers for initial 1+1
                n = fn1+fn2
                # reassign the values fibonacci
                fn1 = fn2
                fn2 = n
                # discount the counter for iterations
                num -= 1
                # transfor number to string for slicing
                s = str(n)
                # convert to list the first and las 9 numbers
                s1, s2 = list(s[:9]), list(s[-9:])
                # order the list values
                s1.sort(reverse=False)
                s2.sort(reverse=False)
                # apply the validation for pandigital number
                v_pan_digital1 = self.__ispandigital(s1)
                v_pan_digital2 = self.__ispandigital(s2)
                # validate the len for function pan digital for know if fibonacci
                # number generated is pan digital
                if v_pan_digital1 == 9 and v_pan_digital2 == 9:
                    print('The first number pan digital '
                          f'in its first {s1} and last {s2} 9 numbers is: {n}')
                    break
                else:
                    print(f"the first and last 9 numbers doesn't pan digital for {n}")
                    continue

        except Exception as e:
            print('An error has occurred in fn fibonacci: ', e)


if __name__ == '__main__':
    num = int(input('Ingrese valor fibonnaci'),)
    func = TestFibonacci(num)
    func.fk()
