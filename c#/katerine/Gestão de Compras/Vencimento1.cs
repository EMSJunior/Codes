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
    public partial class Vencimento1 : Form
    {
        private Vencimento1()
        {
            InitializeComponent();
            try
            {
                List<Compra> notas = new List<Compra>();

                foreach (var compra in BancoDeDados.Compras)
                {
                    if ((compra.Vencimento - DateTime.Now).Days <= 1)
                    {
                        notas.Add(compra);
                    }
                }

                dgvVenci1.DataSource = notas;
                dgvVenci1.Refresh();
            }
            catch { }
        }
        private static Vencimento1 instance { get; set; }
        public static Vencimento1 GetInstance()
        {

            if (instance == null || instance.IsDisposed)
            {
                instance = new Vencimento1();
            }
            return instance;
        }

        private void dgvVenci1_DataSourceChanged(object sender, EventArgs e)
        {

        }
    }
}
