import core

class ArtistGroup(core.model.Model):
	@core.model.exec_query
	def delete_by_member_id(self, member_id):
		return ('DELETE FROM artist_group WHERE memberid = %s', [member_id])

	@core.model.exec_query
	def add(self, group_id, member_id):
		return ('INSERT INTO artist_group (groupid, memberid) VALUES (%s, %s)', [group_id, member_id])
