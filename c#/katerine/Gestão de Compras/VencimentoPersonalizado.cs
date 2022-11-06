using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Gestão_de_Compras
{
    public partial class VencimentoPersonalizado : Form
    {
        private VencimentoPersonalizado()
        {
            InitializeComponent();
        }
        private static VencimentoPersonalizado instance { get; set; }
        public static VencimentoPersonalizado GetInstance()
        {

            if (instance == null || instance.IsDisposed)
            {
                instance = new VencimentoPersonalizado();
            }
            return instance;
        }

        private void VencimentoPersonalizado_Load(object sender, EventArgs e)
        {

        }

        private void txtVencimento1_TextChanged(object sender, EventArgs e)
        {
            try
            {
                var dias = Convert.ToInt16(txtVencimento1.Text);
                List<Compra> notas = new List<Compra>();

                foreach (var compra in BancoDeDados.Compras)
                {
                    if ((compra.Vencimento - DateTime.Now).Days <= dias)
                    { 
                        notas.Add(compra);
                    }
                }

                dataGridView1.DataSource = notas;
                dataGridView1.Refresh();
            }
            catch { }

        }
    }
}
