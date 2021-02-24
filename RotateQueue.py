def RotateQueue(queue, N):
    if queue.size():
        rotation = N % queue.size()
        for i in range(rotation):
            queue.enqueue(queue.dequeue())
