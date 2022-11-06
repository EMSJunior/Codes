using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ControleDeNotas
{
    public partial class Home : Form
    {
        public Home()
        {
            InitializeComponent();
            IsMdiContainer = true;
        }

        private void btnSobre_Click(object sender, EventArgs e)
        {
            Sobre P = Sobre.GetInstance();
            if (P.MdiParent == null)
            {
                P.MdiParent = this;
                P.Show();
            }
            else
            {
                P.WindowState = FormWindowState.Normal;
            }
            P.Activate();
        }

        private void btnSair_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void btnNewNota_Click(object sender, EventArgs e)
        {
            NovaNota P = NovaNota.GetInstance();
            if (P.MdiParent == null)
            {
                P.MdiParent = this;
                P.Show();
            }
            else
            {
                P.WindowState = FormWindowState.Normal;
            }
            P.Activate();

        }

        private void btnLotes_Click(object sender, EventArgs e)
        {
            Vencimentos P = Vencimentos.GetInstance(-1);
            if (P.MdiParent == null)
            {
                P.MdiParent = this;
                P.Show();
            }
            else
            {
                P.WindowState = FormWindowState.Normal;
            }
            P.Activate();
        }

        private void btn1dia_Click(object sender, EventArgs e)
        {
            Vencimentos P = Vencimentos.GetInstance(1);
            if (P.MdiParent == null)
            {
                P.MdiParent = this;
                P.Show();
            }
            else
            {
                P.WindowState = FormWindowState.Normal;
            }
            P.Activate();

        }

        private void btn5dias_Click(object sender, EventArgs e)
        {
            Vencimentos P = Vencimentos.GetInstance(5);
            if (P.MdiParent == null)
            {
                P.MdiParent = this;
                P.Show();
            }
            else
            {
                P.WindowState = FormWindowState.Normal;
            }
            P.Activate();

        }

        private void btnVenci_Click(object sender, EventArgs e)
        {
            Vencimentos P = Vencimentos.GetInstance();
            if (P.MdiParent == null)
            {
                P.MdiParent = this;
                P.Show();
            }
            else
            {
                P.WindowState = FormWindowState.Normal;
            }
            P.Activate();

        }

    }
}
