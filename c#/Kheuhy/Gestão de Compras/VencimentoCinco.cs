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
    public partial class VencimentoCinco : Form
    {
        public VencimentoCinco()
        {
            InitializeComponent();
            try
            {
                List<Compras> notas = new List<Compras>();

                foreach (var compra in BancoDeDados.Compras)
                {
                    if ((compra.Vencimento - DateTime.Now).Days <= 5)
                    {
                        notas.Add(compra);
                    }
                }

                dgvVencimentoCinco.DataSource = notas;
                dgvVencimentoCinco.Refresh();
            }
            catch { }
        }
        public static VencimentoCinco instance { get; set; }

        public static VencimentoCinco GetInstance()
        {
            if (instance == null
                || instance.IsDisposed)
            {
                instance = new VencimentoCinco();
            }
            return instance;
        }
    }
}
