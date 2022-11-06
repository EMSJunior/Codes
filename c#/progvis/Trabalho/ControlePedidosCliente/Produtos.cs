using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ControlePedidosCliente
{
    public partial class Produtos : Form
    {
        private Produtos()
        {
            InitializeComponent();

            lbBdProdutos.DataSource = BD.Produtos;
        }

        
        private static Produtos inst;
        public static Produtos GetForm()
        {
            if (inst == null || inst.IsDisposed)
                inst = new Produtos();
            return inst;
        }
    }
}
