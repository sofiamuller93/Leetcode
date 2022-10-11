class Solution:
    def interpret(self, command: str) -> str:
        cmd_1 = command.replace('()','o')
        cmd_2 = cmd_1.replace('(al)','al')
        return cmd_2
            
            