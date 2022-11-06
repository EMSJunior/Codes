﻿using System;
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
    }
}
