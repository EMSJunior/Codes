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
        public VencimentoPersonalizado()
        {
            InitializeComponent();
        }
        public static VencimentoPersonalizado instance { get; set; }
        public static VencimentoPersonalizado GetInstance()
        {
            if (instance == null
                || instance.IsDisposed)
            {
                instance = new VencimentoPersonalizado();
            }
            return instance;
        }

        private void txtVenci_TextChanged(object sender, EventArgs e)
        {
            try
            {
                var dias = Convert.ToInt16(txtVenci.Text);
                List<Compras> notas = new List<Compras>();

                foreach (var compra in BancoDeDados.Compras)
                {
                    if ((compra.Vencimento - DateTime.Now).Days <= dias)
                    {
                        notas.Add(compra);
                    }
                }

                dtgvVencimentoPersonalizado.DataSource = notas;
                dtgvVencimentoPersonalizado.Refresh();
            }
            catch { }
        }
    }
}
