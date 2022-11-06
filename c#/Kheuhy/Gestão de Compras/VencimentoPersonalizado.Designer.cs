namespace Gestão_de_Compras
{
    partial class VencimentoPersonalizado
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.dtgvVencimentoPersonalizado = new System.Windows.Forms.DataGridView();
            this.lblVencimentop = new System.Windows.Forms.Label();
            this.txtVenci = new System.Windows.Forms.TextBox();
            ((System.ComponentModel.ISupportInitialize)(this.dtgvVencimentoPersonalizado)).BeginInit();
            this.SuspendLayout();
            // 
            // dtgvVencimentoPersonalizado
            // 
            this.dtgvVencimentoPersonalizado.AllowUserToAddRows = false;
            this.dtgvVencimentoPersonalizado.AllowUserToDeleteRows = false;
            this.dtgvVencimentoPersonalizado.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dtgvVencimentoPersonalizado.Location = new System.Drawing.Point(12, 12);
            this.dtgvVencimentoPersonalizado.Name = "dtgvVencimentoPersonalizado";
            this.dtgvVencimentoPersonalizado.ReadOnly = true;
            this.dtgvVencimentoPersonalizado.Size = new System.Drawing.Size(451, 193);
            this.dtgvVencimentoPersonalizado.TabIndex = 0;
            // 
            // lblVencimentop
            // 
            this.lblVencimentop.AutoSize = true;
            this.lblVencimentop.Location = new System.Drawing.Point(12, 231);
            this.lblVencimentop.Name = "lblVencimentop";
            this.lblVencimentop.Size = new System.Drawing.Size(83, 13);
            this.lblVencimentop.TabIndex = 2;
            this.lblVencimentop.Text = "Vencimento em:";
            // 
            // txtVenci
            // 
            this.txtVenci.Location = new System.Drawing.Point(102, 231);
            this.txtVenci.Name = "txtVenci";
            this.txtVenci.Size = new System.Drawing.Size(100, 20);
            this.txtVenci.TabIndex = 3;
            this.txtVenci.TextChanged += new System.EventHandler(this.txtVenci_TextChanged);
            // 
            // VencimentoPersonalizado
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(477, 276);
            this.Controls.Add(this.txtVenci);
            this.Controls.Add(this.lblVencimentop);
            this.Controls.Add(this.dtgvVencimentoPersonalizado);
            this.Name = "VencimentoPersonalizado";
            this.Text = "VencimentoPersonalizado";
            ((System.ComponentModel.ISupportInitialize)(this.dtgvVencimentoPersonalizado)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView dtgvVencimentoPersonalizado;
        private System.Windows.Forms.Label lblVencimentop;
        private System.Windows.Forms.TextBox txtVenci;
    }
}