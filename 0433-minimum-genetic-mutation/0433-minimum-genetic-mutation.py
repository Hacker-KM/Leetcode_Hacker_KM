class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        queue = deque([(startGene, 0)])
        while queue:
            gene,stage = queue.popleft()
            if gene == endGene:
                return stage
            for i in range(len(gene)):
                for nuc in ['A','C','G','T']:
                    if gene[i]!=nuc:
                        tempGene = gene[:i]+nuc+gene[i+1:]
                        if tempGene in bank:
                            queue.append((tempGene,stage+1))
                            bank.remove(tempGene)   
        return -1    