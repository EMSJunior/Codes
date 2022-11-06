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
    public partial class Pedidos : Form
    {
        private Pedidos()
        {
            InitializeComponent();
        }
        private static Pedidos inst;
        public static Pedidos GetForm()
        {
                if (inst == null || inst.IsDisposed)
                    inst = new Pedidos();
            return inst;
        }

        private void btnNew_Click(object sender, EventArgs e)
        {
            var j = CadastroDeItem.GetForm();
            if (j.MdiParent == null)
            {
                j.MdiParent = this.MdiParent;
                j.Show();
            }
            else
            {
                j.WindowState = FormWindowState.Normal;
            }
            j.Activate();
        }
    }
}
