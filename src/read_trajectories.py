def read_snapshots(filename):
    snapshots = []
    current_snapshot = []

    with open(filename, 'r') as file:
        data = [line.strip().split() for line in file if line.strip()]

    for line in data:
        if line[:2] == ['ITEM:', 'TIMESTEP']:
            if current_snapshot:
                snapshots.append(current_snapshot)
                current_snapshot = []
        current_snapshot.append(line)
    
    if current_snapshot:
        snapshots.append(current_snapshot)

    return snapshots
