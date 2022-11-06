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
    public partial class Sobre : Form
    {
        private Sobre()
        {
            InitializeComponent();
        }
        private static Sobre instance { get; set; }
        public static Sobre GetInstance()
        {

            if (instance == null || instance.IsDisposed)
            {
                instance = new Sobre();
            }
            return instance;
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start("mailto:jumendessouza1@gmail.com");
        }
    }
}
