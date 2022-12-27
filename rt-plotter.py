import numpy as np
import matplotlib.pyplot as plt

def rtplotter(func, val, rad=True, sf=10):
    adj = None
    opp = None
    hyp = None
    if not rad:
        value = np.radians(val)
    if func == 'sin':
        opp = np.sin(val)
        hyp = 1
        adj = np.sqrt(hyp**2 - opp**2)
    elif func == 'cos':
        adj = np.cos(val)
        hyp = 1
        opp= np.sqrt(hyp**2 - adj**2)
    elif func == 'tan':
        opp = np.sin(val)
        adj = np.cos(val)
        hyp = opp / adj
    elif func == 'sec':
        adj = 1 / np.cos(val)
        hyp = 1
        opp = np.sqrt(hyp**2 - adj**2)
    elif func == 'csc':
        opp = 1 / np.sin(val)
        hyp = 1
        adj = np.sqrt(hyp**2 - opp**2)
    elif func == 'cot':
        opp = np.sin(val)
        adj = np.cos(val)
        hyp = adj / opp
    else:
        raise ValueError('Incomplete input.')
    
    val_rad = np.radians(val)
    opp_str = f'{opp:.{sf}f}'
    hyp_str = f'{hyp:.{sf}f}'
    adj_str = f'{adj:.{sf}f}'
    
    plt.style.use('seaborn-notebook')
    fig, rtplotter = plt.subplots(facecolor='aliceblue', figsize=(16, 9))
    rtplotter.set_title('Result of Reference Triangle Plotting', font = 'Arial', fontweight='bold', fontsize=20)
    rtplotter.set_facecolor('ivory')
    rtplotter.axhline(y = 0, c='darkslategrey', lw=3.5)
    rtplotter.axvline(x = 0, c='darkslategrey', lw=3.5)
    rtplotter.set_xlabel('Abscissa', font = 'Arial', fontweight='bold', style='italic', fontsize=16)
    rtplotter.set_ylabel('Ordinate', font = 'Arial', fontweight='bold', style='italic', fontsize=16)
    rtplotter.grid(color='dodgerblue', linestyle='--')
    rtplotter.plot([0, adj], [0, opp], c='r', lw=5)
    rtplotter.plot([adj, adj], [opp, 0], c='b', lw=5)
    rtplotter.plot([adj, 0], [0, 0], c='g', lw=5)
    plt.show()
    
    print(f'Degrees = {val}, Radians = {val_rad}')
    print(f'Adjacent = {adj}, Opposite = {opp}, Hypotenuse = {hyp}')

rtplotter('sin', 45)
