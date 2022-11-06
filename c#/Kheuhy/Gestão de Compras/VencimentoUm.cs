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
    public partial class VencimentoUm : Form
    {
        public VencimentoUm()
        {
            InitializeComponent();
            try
            {
                List<Compras> notas = new List<Compras>();

                foreach (var compra in BancoDeDados.Compras)
                {
                    if ((compra.Vencimento - DateTime.Now).Days <= 1)
                    {
                        notas.Add(compra);
                    }
                }

                dgvVencimentoUm.DataSource = notas;
                dgvVencimentoUm.Refresh();
            }
            catch { }
        }
        public static VencimentoUm instance { get; set; }

        public static VencimentoUm GetInstance()
        {
            if (instance == null
                || instance.IsDisposed)
            {
                instance = new VencimentoUm();
            }
            return instance;
        }
    }
}
