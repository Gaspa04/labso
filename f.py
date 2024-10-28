from collections import deque

def fifo(pages, frames):
    memory = deque(maxlen=frames)
    faults = 0
    for page in pages:
        if page not in memory:
            faults += 1
            memory.append(page)
    return faults

def lru(pages, frames):
    memory = []
    faults = 0
    for page in pages:
        if page in memory:
            memory.remove(page)
        else:
            if len(memory) >= frames:
                memory.pop(0)  # Remove a página menos recentemente usada
                faults += 1
            faults += 1
        memory.append(page)
    return faults

def optimal(pages, frames):
    memory = []
    faults = 0
    for i in range(len(pages)):
        page = pages[i]
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                # Encontrar a página que será utilizada mais tarde ou nunca mais
                farthest = i
                index_to_remove = 0
                for j in range(len(memory)):
                    try:
                        next_use = pages[i+1:].index(memory[j])
                    except ValueError:
                        next_use = float('inf')  # Página não será mais usada
                    if next_use > farthest:
                        farthest = next_use
                        index_to_remove = j
                memory[index_to_remove] = page
            faults += 1
    return faults

# Parâmetros da simulação
pages = [1, 2, 3, 4, 2, 1, 5, 6, 2, 1, 2, 3, 7, 6, 3, 2, 1, 2, 3, 6]
frames = 3

# Simulação dos algoritmos
fifo_faults = fifo(pages, frames)
lru_faults = lru(pages, frames)
optimal_faults = optimal(pages, frames)

print(f"FIFO: {fifo_faults} faltas de página")
print(f"LRU: {lru_faults} faltas de página")
print(f"ÓTIMO: {optimal_faults} faltas de página")
