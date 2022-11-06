namespace Gestão_de_Compras
{
    partial class Vencimento5
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
            this.panel1 = new System.Windows.Forms.Panel();
            this.lblVencimento1 = new System.Windows.Forms.Label();
            this.dgvVenci5 = new System.Windows.Forms.DataGridView();
            this.panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dgvVenci5)).BeginInit();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.lblVencimento1);
            this.panel1.Controls.Add(this.dgvVenci5);
            this.panel1.Location = new System.Drawing.Point(21, 22);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(455, 233);
            this.panel1.TabIndex = 0;
            // 
            // lblVencimento1
            // 
            this.lblVencimento1.AutoSize = true;
            this.lblVencimento1.Location = new System.Drawing.Point(341, 173);
            this.lblVencimento1.Name = "lblVencimento1";
            this.lblVencimento1.Size = new System.Drawing.Size(111, 13);
            this.lblVencimento1.TabIndex = 1;
            this.lblVencimento1.Text = "Vencimento em 5 dias";
            // 
            // dgvVenci5
            // 
            this.dgvVenci5.AllowUserToAddRows = false;
            this.dgvVenci5.AllowUserToDeleteRows = false;
            this.dgvVenci5.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvVenci5.Location = new System.Drawing.Point(3, 3);
            this.dgvVenci5.Name = "dgvVenci5";
            this.dgvVenci5.ReadOnly = true;
            this.dgvVenci5.Size = new System.Drawing.Size(449, 150);
            this.dgvVenci5.TabIndex = 0;
            // 
            // Vencimento5
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(518, 283);
            this.Controls.Add(this.panel1);
            this.Name = "Vencimento5";
            this.Text = "Vencimento em 5 dias";
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dgvVenci5)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.DataGridView dgvVenci5;
        private System.Windows.Forms.Label lblVencimento1;
    }
}