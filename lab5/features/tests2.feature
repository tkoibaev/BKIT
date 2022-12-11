Feature: testing roots

    Scenario Outline: multiple roots roots
        Given <a> coef a, coef b is <b> and c is <c>
        When starting function
        Then we shoud see <result>

        Examples:
            | a  | b   | c  | result         |
            | 1  | 10  | 11 | "[]"           |
            | 10 | 0   | 0  | "[0]"          |
            | 1  | -2  | -8 | "[-2, 2]"      |
            | 4  | 16  | 0  | "[-2, 0, 2]"   |
            | 1  | -10 | 9  | "[-3, 1, 1, 3]"|