//
//  notifTableViewCell.swift
//  LiveHive
//
//  Created by Brianna Butler on 9/29/20.
//  Copyright © 2020 LiveHive. All rights reserved.
//

import UIKit

class notifTableViewCell: UITableViewCell {
    @IBOutlet weak var userPic: UIImageView!
    
    @IBOutlet weak var actionPic: UIImageView!
    
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
        
        userPic.layer.masksToBounds = true
        userPic.layer.cornerRadius = userPic.bounds.width / 2
    }

    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }

}
