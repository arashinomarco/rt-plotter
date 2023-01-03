import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def dmsdeg(d, m, s):
    return d + m / 60 + s / 3600

def rtplotter(func, val, sf=20):
    val_rad = np.radians(val)
    
    if func == 'sin':
        opp = np.sin(val_rad)
        hyp = 1
        adj = np.sqrt(hyp**2 - opp**2)
    elif func == 'cos':
        adj = np.cos(val_rad)
        hyp = 1
        opp= np.sqrt(hyp**2 - adj**2)
    elif func == 'tan':
        opp = np.sin(val_rad)
        adj = np.cos(val_rad)
        hyp = opp / adj
    elif func == 'sec':
        adj = 1 / np.cos(val_rad)
        hyp = 1
        opp = np.sqrt(hyp**2 - adj**2)
    elif func == 'csc':
        opp = 1 / np.sin(val_rad)
        hyp = 1
        adj = np.sqrt(hyp**2 - opp**2)
    elif func == 'cot':
        opp = np.sin(val_rad)
        adj = np.cos(val_rad)
        hyp = adj / opp
    else:
        raise ValueError(f'Function "{func}" is not available.')

    opp_str = f'{opp:.{sf}f}'
    hyp_str = f'{hyp:.{sf}f}'
    adj_str = f'{adj:.{sf}f}'
    sin_str = f'{np.sin(val_rad):.{sf}f}'
    cos_str = f'{np.cos(val_rad):.{sf}f}'
    tan_str = f'{np.tan(val_rad):.{sf}f}'
    sec_str = f'{1 / np.cos(val_rad):.{sf}f}'
    csc_str = f'{1 / np.sin(val_rad):.{sf}f}'
    cot_str = f'{1 / np.tan(val_rad):.{sf}f}'

    plt.style.use('seaborn-notebook')
    fig, rtplotter = plt.subplots(facecolor='aliceblue', figsize=(8, 8))
    rtplotter.set_title('Result of Reference Triangle Plotting', font = 'Arial', fontweight='bold', fontsize=15)
    rtplotter.set_facecolor('ivory')
    rtplotter.axhline(y = 0, c='silver', lw=1.75)
    rtplotter.axvline(x = 0, c='silver', lw=1.75)
    rtplotter.set_xlim(-1.5, 1.5)
    rtplotter.set_ylim(-1.5, 1.5)
    rtplotter.set_xlabel('Abscissa', font = 'Arial', fontweight='bold', style='italic', fontsize=12)
    rtplotter.set_ylabel('Ordinate', font = 'Arial', fontweight='bold', style='italic', fontsize=12)
    rtplotter.grid(color='dodgerblue', linestyle='--')
    rtplotter.plot([0, adj], [0, opp], c='r', lw=2.5)
    rtplotter.plot([adj, adj], [opp, 0], c='b', lw=2.5)
    rtplotter.plot([adj, 0], [0, 0], c='g', lw=2.5)
    
    unito = Circle((0, 0), radius=1, fill=False, color='k', lw=1.75)
    rtplotter.add_patch(unito)
    
    plt.show()
    
    print(f'Degrees = {val}, Radians = {val_rad}')
    print(f'Adjacent = {adj_str}, Opposite = {opp_str}, Hypotenuse = {hyp_str}\n')
    print(f'Sine = {sin_str}, Cosine = {cos_str}, Tangent = {tan_str}')
    print(f'Secant = {sec_str}, Cosecant = {csc_str}, Cotangent = {cot_str}')

dms = (15, 0, 0)
val = dmsdeg(*dms)
rtplotter('sin', val)

if __name__=="__rtplotter__":
    rtplotter()
